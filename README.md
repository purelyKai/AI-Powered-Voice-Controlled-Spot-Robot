# AI-Powered Voice-Controlled Spot Robot (Cal-Hacks-11.0)

## Abstract:
This project explores the use of Boston Dynamics’ Spot robot, integrating AI and voice control to assist in navigating complex environments. The Python-based application processes voice commands through Deepgram's speech-to-text API and utilizes Groq’s AI API to determine the robot's movement actions. The robot executes these actions using the Boston Dynamics Spot SDK. The current implementation showcases the ability to control Spot via voice commands, laying a foundation for future development as an assistive technology.

## Features:
- **Voice Command Input**: Users provide voice commands to control the robot’s movements.
- **Speech-to-Text Processing**: Audio is converted to text using the Deepgram API.
- **AI-Powered Decision Making**: Groq's AI API processes text commands to determine movement sequences.
- **Robot Movement Execution**: Commands are sent to Spot using the Boston Dynamics Spot SDK.
- **Docker Integration**: The application is containerized using Docker and runs on Spot’s onboard computer.

## Tech Stack:
- **Hardware**: Boston Dynamics Spot robot
- **APIs**:
  - **Deepgram**: Speech-to-text conversion
  - **Groq**: AI-based decision making for movement
  - **Boston Dynamics Spot SDK**: For robot control
- **Programming Language**: Python
- **Containerization**: Docker
- **Platform**: Runs on Spot’s onboard computer

## Things to Consider:
- Current version only includes voice commands and robot movement.
- Further development could involve more complex navigation logic, multi-modal feedback (audio/tactile), and integration with Fetch.ai for real-time path planning.

## Future Work:
- **Enhanced Command Recognition**: Add sentiment detection or context for better alignment of verbal inputs with actions.
- **Multi-modal Feedback**: Implement audio and tactile feedback to improve user interaction.
- **Path Planning**: Integrate Fetch.ai for dynamic navigation and obstacle avoidance on a large scale (i.e. the city or surrounding blocks).
