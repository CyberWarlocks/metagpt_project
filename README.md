# MetaGPT Project

This is a MetaGPT-based project.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure the project:
   - Edit `config/config.yaml` to set your OpenAI API key and other configurations.

3. Run the project:
   ```
   python src/main.py
   ```

## Project Structure

- `config/`: Configuration files
- `src/`: Source code
  - `roles/`: Custom role definitions
  - `tasks/`: Task definitions
- `data/`: Data files
- `tests/`: Test files

## Customization

- Add custom roles in `src/roles/`
- Define tasks in `src/tasks/`
- Modify `src/main.py` to use your custom roles and tasks

