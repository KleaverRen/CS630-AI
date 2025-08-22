import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(timezone: str) -> dict:
    """Retrieves the current time for a specified timezone.

    Args:
        timezone (str): The timezone for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    try:
        tz = ZoneInfo(timezone)
        current_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return {
            "status": "success",
            "current_time": f"The current time in {timezone} is {current_time}.",
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Could not retrieve time for timezone '{timezone}': {str(e)}",
        }


root_agent = Agent(
    name="multi_tool_agent_with_vocie",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-live-2.5-flash-preview",
    description="Agent to answer questions abouts time and weather in the city.",
    instruction="""
    You are a helpful assistant who can answer questions about the time and weather in the city.
    """,
    tools=[get_weather, get_current_time],
)
