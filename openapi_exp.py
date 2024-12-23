
import tiktoken
import pickle
from openai import OpenAI
# Set your OpenAI API key
#openai.api_key = "your_openai_api_key"

# Function to calculate tokens
def calculate_tokens(file_content, model_name="gpt-4"):
    tokenizer = tiktoken.encoding_for_model(model_name)
    tokens = tokenizer.encode(file_content)
    return len(tokens)

# Path to the input file
file_path = "/home/noaman/code/muslimkids/code_prompts/code/apps/profiles/models.py"

# Read the file content
with open(file_path, "r") as file:
    code = file.read()

# Calculate input tokens
model_name = "gpt-4o"  # Specify the model
input_tokens = calculate_tokens(code, model_name=model_name)
print(f"Input file contains {input_tokens} tokens.")

# Ensure the file fits within the model's limit
token_limit = 30000  # Token limit for GPT-4
if input_tokens * 2 > token_limit:
    raise ValueError(f"File size exceeds the model's token limit of {token_limit}. Please split the file.")

# Prepare the combined prompt
prompt = f"""
You are a highly skilled Python and Django developer tasked with upgrading a Django project from version 1.11 to 5.0 and ensuring compatibility with Python 3.12. Follow best practices, handle deprecations, and provide clear, actionable comments explaining each change. Your output must be production-ready.

--- Upgrading Task ---
Upgrade the provided Django project’s imports and models code to make them fully compatible with Django 5.0 and Python 3.12. Follow these requirements:

1. **Django Imports:**
    - Update imports to align with Django 5.0 standards.
    - Remove deprecated modules and replace them with their recommended alternatives.
    - Update module paths that have changed between Django 1.11 and Django 5.0.

2. **Python Imports:**
    - Ensure compatibility with Python 3.12.
    - Replace deprecated modules or methods with updated versions.
    - Use modern best practices, such as:
        - Using `collections.abc` for importing ABCs like `Iterable` and `Mapping`.
        - Using `importlib` or `pathlib` for relevant operations.

3. **Models Code:**
    - Replace `NullBooleanField` with `BooleanField(null=True)`.
    - Add the `on_delete` argument to all `ForeignKey` and `OneToOneField` fields.
    - Update `ugettext_lazy` to `gettext_lazy`.
    - Ensure `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` where applicable.
    - Remove outdated decorators like `@models.permalink` and modernize their logic.

4. **Comment Changes:**
    - Clearly comment on every update made, explaining the reason and relevance of the change.

---

Provided Code:
```python
{code}
```
"""
import pdb;pdb.set_trace()
# Create OpenAI API request
messages = [
    {"role": "system", "content": "You are a helpful assistant for upgrading Django projects to newer versions."},
    {"role": "user", "content": prompt}
]

# Call the OpenAI API
client = OpenAI()
response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    max_tokens=15000  # Adjust based on the expected output size
)



# Save the response to a file
with open("response.pickle", "wb") as pickle_file:
    pickle.dump(response, pickle_file)

# Extract and save the output content
output_file_path = "/home/noaman/code/muslimkids/code_prompts/code/apps/profiles/processed_models-1.py"
with open(output_file_path, "w") as output_file:
    output_file.write(response['choices'][0].message.content)

print(f"Processed file saved at: {output_file_path}")
