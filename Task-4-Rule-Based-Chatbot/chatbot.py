
import json
import re
from pathlib import Path


def load_faqs():
    file_path = Path(__file__).parent / "faq.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def normalize_input(user_input):
    return user_input.lower().strip()


def detect_intents(user_input, data):
    text = normalize_input(user_input)
    intents = []

    # Detect greetings
    for greeting in data.get("greetings", []):
        pattern = r"\b" + re.escape(greeting) + r"\b"
        if re.search(pattern, text):
            intents.append("greeting")
            break

    # Detect business hours questions
    if re.search(
        r"\b(hours?|timings?|open|opening|closing|close|working hours)\b",
        text
    ):
        intents.append("hours")

    # Detect project submission questions
    if re.search(
        r"\b(submit|submission|upload|github|project|workspace)\b",
        text
    ):
        intents.append("project")

    # Detect certificate questions
    if re.search(
        r"\b(certificate|certificates|certification|issued|receive)\b",
        text
    ):
        if re.search(
            r"\b(certificate|certificates|certification)\b",
            text
        ):
            intents.append("certificate")

    return intents


def get_response(intents, data):
    responses = []
    faqs = data.get("faqs", [])

    if "greeting" in intents:
        responses.append(
            "Hello! Welcome to the internship support assistant."
        )

    for intent in intents:
        if intent == "hours" and len(faqs) > 0:
            responses.append(faqs[0]["answer"])

        elif intent == "project" and len(faqs) > 1:
            responses.append(faqs[1]["answer"])

        elif intent == "certificate" and len(faqs) > 2:
            responses.append(faqs[2]["answer"])

    if not responses:
        return (
            "Sorry, I didn't understand your question.\n"
            "Please ask about business hours, project submission, "
            "or certificates. Type 'help' for more options."
        )

    return "\n".join(responses)


def show_faqs(data):
    print("Bot: Here are the available FAQs:")

    for number, faq in enumerate(data.get("faqs", []), start=1):
        print(str(number) + ". " + faq["question"])


def show_history(history):
    if not history:
        print("Bot: No conversation history yet.")
        return

    print("\nBot: Conversation History")

    for item in history:
        print("You:", item["user"])
        print("Bot:", item["bot"])


def main():
    try:
        data = load_faqs()
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print("Error loading faq.json:", error)
        return

    print("=" * 48)
    print("       INTERNSHIP SUPPORT CHATBOT")
    print("=" * 48)
    print("Ask about business hours, project submission,")
    print("or certificates.")
    print("Commands: help, faq, history, bye, exit, quit")
    print("\nBot: Hello! How can I help you today?")

    history = []
    user_name = ""

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day.")
            break

        if not user_input:
            print("Bot: Please enter a question.")
            continue

        text = normalize_input(user_input)

        # Exit commands
        if re.fullmatch(
            r"(good\s*bye|bye|exit|quit)[.! ]*",
            text
        ):
            print("Bot: Goodbye! Have a great day.")
            break

        # Help command
        if text == "help":
            response = (
                "You can ask me about:\n"
                "1. Business hours\n"
                "2. Internship project submission\n"
                "3. Certificate delivery\n"
                "Commands: faq, history, name, help, bye"
            )
            print("Bot:", response)
            history.append({"user": user_input, "bot": response})
            continue

        # Display FAQ questions
        if text in ("faq", "faqs", "show faq", "show faqs"):
            show_faqs(data)
            response = "Displayed the available FAQ questions."
            history.append({"user": user_input, "bot": response})
            continue

        # Display conversation history
        if text == "history":
            show_history(history)
            continue

        # Ask for and remember the user's name
        if text in ("name", "my name"):
            if user_name:
                response = "Your name is " + user_name + "."
            else:
                response = "I don't know your name yet. Type: my name is Pavan"
            print("Bot:", response)
            history.append({"user": user_input, "bot": response})
            continue

        name_match = re.fullmatch(
            r"my name is\s+([a-zA-Z][a-zA-Z ]{0,39})[.! ]*",
            user_input,
            re.IGNORECASE
        )

        if name_match:
            user_name = name_match.group(1).strip().title()
            response = "Nice to meet you, " + user_name + "!"
            print("Bot:", response)
            history.append({"user": user_input, "bot": response})
            continue

        # Detect and answer user intents
        intents = detect_intents(user_input, data)
        response = get_response(intents, data)

        if user_name:
            response = response.replace(
                "Hello! Welcome",
                "Hello, " + user_name + "! Welcome"
            )

        print("Bot:", response)

        history.append({
            "user": user_input,
            "bot": response
        })


if __name__ == "__main__":
    main()
