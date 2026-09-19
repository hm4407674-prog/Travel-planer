import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0;
        }

        .subtitle {
            font-size: 1.05rem;
            color: #6b7280;
            margin-bottom: 2rem;
        }

        .section-title {
            font-size: 1.45rem;
            font-weight: 650;
            margin-top: 1.8rem;
            margin-bottom: 0.8rem;
        }

        .info-card {
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(128,128,128,0.25);
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌍 Travel Planner</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Explore destinations, check live weather, manage your budget, "
    "and view your destination on an interactive map."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# API CONFIGURATION
# ============================================================

GEOCODING_API = (
    "https://geocoding-api.open-meteo.com/v1/search"
)

WEATHER_API = (
    "https://api.open-meteo.com/v1/forecast"
)

REQUEST_TIMEOUT = 10


# ============================================================
# CITY SEARCH
# ============================================================

@st.cache_data(ttl=3600)
def find_city(city_name):
    """
    Search for a city using the Open-Meteo geocoding API.
    """

    try:
        response = requests.get(
            GEOCODING_API,
            params={
                "name": city_name,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("results")

        if not results:
            return None

        place = results[0]

        return {
            "name": place.get("name", city_name),
            "country": place.get("country", "Unknown"),
            "latitude": place["latitude"],
            "longitude": place["longitude"],
        }

    except (requests.RequestException, KeyError, ValueError):
        return None


# ============================================================
# WEATHER DATA
# ============================================================

@st.cache_data(ttl=1800)
def get_weather(latitude, longitude):
    """
    Retrieve current weather and a five-day forecast.
    """

    try:
        response = requests.get(
            WEATHER_API,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "wind_speed_10m"
                ),
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min"
                ),
                "timezone": "auto",
                "forecast_days": 5,
            },
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:
        return None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("✈️ Trip Settings")

    city_input = st.text_input(
        "🔍 Destination",
        value="Tokyo",
        placeholder="Enter a city...",
    )

    budget = st.number_input(
        "💰 Total Budget ($)",
        min_value=0,
        max_value=100000,
        value=2000,
        step=100,
    )

    st.divider()

    st.markdown("### ℹ️ About")

    st.caption(
        "Travel Planner provides destination coordinates, "
        "current weather, a five-day forecast, and an "
        "interactive map."
    )

    st.caption(
        "Weather data: Open-Meteo"
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

if city_input.strip():

    # --------------------------------------------------------
    # FIND DESTINATION
    # --------------------------------------------------------

    with st.spinner("🔎 Searching for destination..."):

        location = find_city(city_input.strip())

    if location is None:

        st.error(
            "❌ Destination not found."
        )

        st.info(
            "Try entering a major city name, such as "
            "Tokyo, London, Paris, or Addis Ababa."
        )

    else:

        # ----------------------------------------------------
        # WEATHER
        # ----------------------------------------------------

        with st.spinner("🌤️ Loading weather information..."):

            weather = get_weather(
                location["latitude"],
                location["longitude"],
            )

        if weather is None:

            st.error(
                "❌ Weather data could not be retrieved."
            )

        else:

            current = weather.get("current", {})
            daily = weather.get("daily", {})

            temperature = current.get(
                "temperature_2m"
            )

            wind_speed = current.get(
                "wind_speed_10m"
            )

            # ------------------------------------------------
            # DESTINATION HEADER
            # ------------------------------------------------

            st.subheader(
                f"📍 {location['name']}, "
                f"{location['country']}"
            )

            st.caption(
                f"Coordinates: "
                f"{location['latitude']:.4f}, "
                f"{location['longitude']:.4f}"
            )

            # ------------------------------------------------
            # KEY METRICS
            # ------------------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🌡️ Current Temperature",
                    f"{temperature} °C",
                )

            with col2:
                st.metric(
                    "💨 Wind Speed",
                    f"{wind_speed} km/h",
                )

            with col3:
                st.metric(
                    "💰 Travel Budget",
                    f"${budget:,.0f}",
                )

            # ------------------------------------------------
            # FORECAST
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                "📅 5-Day Weather Forecast"
                "</div>",
                unsafe_allow_html=True,
            )

            forecast = pd.DataFrame(
                {
                    "Date": daily.get(
                        "time", []
                    ),
                    "High °C": daily.get(
                        "temperature_2m_max", []
                    ),
                    "Low °C": daily.get(
                        "temperature_2m_min", []
                    ),
                }
            )

            if not forecast.empty:

                forecast["Date"] = (
                    pd.to_datetime(
                        forecast["Date"]
                    ).dt.strftime(
                        "%a, %b %d"
                    )
                )

                forecast["High °C"] = (
                    forecast["High °C"]
                    .round(1)
                )

                forecast["Low °C"] = (
                    forecast["Low °C"]
                    .round(1)
                )

                st.dataframe(
                    forecast,
                    use_container_width=True,
                    hide_index=True,
                )

            # ------------------------------------------------
            # TEMPERATURE CHART
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                "📈 Temperature Trend"
                "</div>",
                unsafe_allow_html=True,
            )

            chart_data = forecast.copy()

            if not chart_data.empty:

                chart_data = chart_data.set_index(
                    "Date"
                )

                st.line_chart(
                    chart_data[
                        ["High °C", "Low °C"]
                    ]
                )

            # ------------------------------------------------
            # MAP
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                "🗺️ Destination Map"
                "</div>",
                unsafe_allow_html=True,
            )

            destination_map = folium.Map(
                location=[
                    location["latitude"],
                    location["longitude"],
                ],
                zoom_start=11,
                control_scale=True,
            )

            folium.Marker(
                [
                    location["latitude"],
                    location["longitude"],
                ],
                popup=folium.Popup(
                    f"""
                    <b>{location['name']}</b><br>
                    {location['country']}<br>
                    🌡️ {temperature} °C<br>
                    💨 {wind_speed} km/h
                    """,
                    max_width=250,
                ),
                tooltip="📍 Destination",
                icon=folium.Icon(
                    icon="info-sign"
                ),
            ).add_to(destination_map)

            st_folium(
                destination_map,
                height=450,
                use_container_width=True,
            )

            # ------------------------------------------------
            # TRIP SUMMARY
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                "📋 Trip Summary"
                "</div>",
                unsafe_allow_html=True,
            )

            summary_col1, summary_col2 = st.columns(2)

            with summary_col1:

                st.write(
                    f"**Destination:** "
                    f"{location['name']}, "
                    f"{location['country']}"
                )

                st.write(
                    f"**Budget:** "
                    f"${budget:,.0f}"
                )

            with summary_col2:

                st.write(
                    f"**Temperature:** "
                    f"{temperature} °C"
                )

                st.write(
                    f"**Wind:** "
                    f"{wind_speed} km/h"
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌍 Travel Planner • "
    "Built with Streamlit, Open-Meteo, Pandas & Folium"
  )
