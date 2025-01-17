# DevAssistant: Your Personal AI Assistant (WIP)

DevAssistant is a work-in-progress project aimed at creating a powerful and efficient Artificial General Intelligence (AGI) that can assist you in various tasks, solve problems, and learn from its experiences. The goal is to build a system that can understand and process complex objectives, break them down into smaller tasks, and execute them autonomously while continuously improving its performance.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Starting a Local Searxng Instance](#starting-a-local-searxng-instance)
- [Components](#components)
- [Workflow](#workflow)
- [Data Flow](#data-flow)
- [Future Improvements](#future-improvements)
- [Risks & Safety Considerations](#risks--safety-considerations)

## Overview

DevAssistant is built on five main components that work together to achieve a given objective. These components are:

1. Perception module
2. Memory module
3. Learning module
4. Reasoning module
5. Execution module

## Installation

Before you can start using DevAssistant, you need to set up the environment by obtaining an OpenAI API key and starting a local Searxng instance.

The [langchain-visualizer](https://github.com/amosjyng/langchain-visualizer) is utilized to display all the LLM calls executed throughout the script's runtime.

Run `python main.py`

### Starting a Local Searxng Instance

Searxng is a privacy-respecting, hackable metasearch engine. It is used as a tool of the execution agent. To start a local Searxng instance, follow these steps:

1. Visit the [Searxng GitHub repository](https://github.com/searxng/searxng).
2. Follow the instructions in the README file to set up and configure Searxng on your local machine.
3. Ensure that `searxng/settings.yml` contains these values:
```yaml
server:
  limiter: false
general:
  debug: true
search:
  formats:
    - html
    - json
```
4. Start the Searxng instance as instructed in the repository.

## Components

DevAssistant is comprised of five main modules that work together to process, analyze, and execute tasks:

1. **Perception module**: Responsible for processing raw data from different sources and extracting relevant features using techniques like computer vision, natural language processing, and speech recognition.
2. **Memory module**: Manages different types of memory, such as short-term, long-term, and procedural memory, allowing efficient storage, retrieval, and updating of information.
3. **Learning module**: Updates the AGI's knowledge and improves its performance over time using techniques like reinforcement learning, supervised learning, and unsupervised learning.
4. **Reasoning module**: Makes decisions, solves problems, and generates new tasks based on the given objective, handling complex reasoning tasks and making inferences from available data.
5. **Execution module**: Carries out tasks generated by the reasoning module, interacting with external systems and performing actions autonomously.

## Workflow

The workflow for DevAssistant consists of the following steps:

1. Receive the objective as input.
2. Pre-process the objective using the perception module to extract relevant features.
3. Use the reasoning module to decompose the objective into smaller sub-goals and tasks.
4. Prioritize tasks and sub-goals based on the AGI's understanding of the problem and the available resources.
5. Execute tasks using the execution module, updating the memory module with the results.
6. Monitor progress towards the objective and evaluate performance using the learning module.
7. If the objective is not yet achieved, adjust the approach based on the learning module's feedback and generate new tasks.
8. Repeat steps 4-7 until the objective is achieved or a stopping condition is reached.
9. Communicate the results and any relevant insights to the user.

## Data Flow

The data flow in DevAssistant can be summarized as follows:

1. Input data is received and pre-processed by the perception module.
2. Processed data is stored and managed by the memory module.
3. The reasoning module uses the data to generate tasks and sub-goals.
4. The execution module performs the tasks and updates the memory module with the results.
5. The learning module evaluates the performance and provides feedback for improvement.

## Future Improvements

Some suggested future improvements for DevAssistant include:

- Integrating a security/safety agent to ensure ethical considerations are met and prevent potential misuse.
- Implementing task sequencing and parallel tasks for improved efficiency.
- Adding interim milestones to track progress more effectively.
- Providing real-time priority updates for better resource allocation.

## Risks & Safety Considerations

Key risks associated with DevAssistant are:

- Data privacy and security: Ensuring user data is protected and not misused.
- Ethical concerns: Ensuring the AI system does not engage in unethical activities.
- Dependence on model accuracy: Ensuring the AI system's performance is reliable and accurate.
- System overload: Preventing the AI system from becoming overwhelmed by too many tasks.
- Misinterpretation of task prioritization: Ensuring the AI system correctly understands and prioritizes tasks.

Addressing these risks is crucial for the successful application of DevAssistant.

# Inspirations and References

- [Auto-GPT](https://github.com/Torantulino/Auto-GPT)
- [babyAGI](https://github.com/yoheinakajima/babyagi)
- [Llama Index](https://github.com/jerryjliu/llama_index)
- [langchain](https://github.com/hwchase17/langchain)
