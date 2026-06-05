# Links

- uv installation instructions: https://docs.astral.sh/uv/getting-started/installation/
- Codex CLI installation instructions: https://developers.openai.com/codex/quickstart
- OpenAI account tiers: https://chatgpt.com/pricing/
- OpenAI API dashboard: https://openai.com/api/

# Prompts

Initial prompt:

 > “Implement the behavior for the button Delete, which should delete the currently highlighted row of the datatable, and implement the behavior for the button Clear All, which should delete all existing contacts.”

Tweak prompt:

 > “Apply the `@on()` decorators directly on the action methods, removing the need for the auxiliary methods `.on_delete_button_pressed()` and `.on_clear_all_button_pressed()`.”

Further refinement prompt:

 > “To prevent accidental deletion of contacts, use the `QuestionDialog` to confirm whenever the user tries to delete one or all contacts.”
