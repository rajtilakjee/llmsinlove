from personas.sally_persona import response_from_sally
from personas.ethan_persona import response_from_ethan


def generate_chat(num_turns):
    # Initial message from Sally to Ethan
    initial_message = "Hi, how are you?"
    print(f"Sally: {initial_message}")

    # Start the conversation
    current_speaker = "Ethan"  # Ethan will respond first
    last_message = initial_message

    # Generate the chat for the specified number of turns
    turn = 0
    while turn < num_turns:
        if current_speaker == "Ethan":
            response = response_from_ethan(last_message)
            print(f"Ethan: {response.content}")
            current_speaker = "Sally"  # Switch to Sally for the next turn
        else:
            response = response_from_sally(last_message)
            print(f"Sally: {response.content}")
            current_speaker = "Ethan"  # Switch to Ethan for the next turn

        last_message = response.content
        turn += 1
        print("\n")


if __name__ == "__main__":
    # Decide how many turns the chat should have
    num_turns = 5  # Change this value to control the number of turns
    generate_chat(num_turns)
