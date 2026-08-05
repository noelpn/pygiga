from pygiga.communication import ConversationManager, PromptManager

if __name__ == '__main__':
    conversation = ConversationManager()
    prompt_manager = PromptManager()
    conversation.add_user_message('Hi there!')
    prompt = prompt_manager.build_text('How are you?', conversation.get_history())
    print(prompt)
