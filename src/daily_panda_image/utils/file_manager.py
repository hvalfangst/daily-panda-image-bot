"""
FileManager - Handles file operations for images, prompts, and README updates.
"""

import datetime
import os
from pathlib import Path


class FileManager:
    """Manages file operations for images, prompts, and README updates."""

    @staticmethod
    def get_project_root() -> Path:
        """
        Get the project root directory.

        Returns:
            Path to project root directory
        """
        # Navigate up 4 levels from the current file location to get to the project root
        return Path(__file__).resolve().parent.parent.parent.parent

    @staticmethod
    def ensure_directory_exists(directory: str) -> None:
        """
        Create directory if it doesn't exist.

        Args:
            directory: Path to directory to create
        """
        dir_path = os.path.join(FileManager.get_project_root(), directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory '{directory}' exists or created successfully.\n")

    @staticmethod
    def save_image(image_bytes: bytes, current_date: datetime.date) -> None:
        """
        Save image with both timestamped and current filenames.

        Args:
            image_bytes: Image data to save
            current_date: Current date for timestamping
        """
        FileManager.ensure_directory_exists("images")

        # Save timestamped version
        timestamped_path = os.path.join(FileManager.get_project_root(), "images", f"panda_{current_date}.png")
        with open(timestamped_path, "wb") as f:
            f.write(image_bytes)
        print(f"Image '{timestamped_path}' saved successfully.\n")

        # Save current version
        current_path = os.path.join(FileManager.get_project_root(), "images", "panda_current.png")
        with open(current_path, "wb") as f:
            f.write(image_bytes)
        print(f"Image '{current_path}' saved successfully.\n")

    @staticmethod
    def save_prompt(prompt: str, current_date: datetime.date) -> None:
        """
        Save prompt with both timestamped and current filenames.

        Args:
            prompt: Prompt text to save
            current_date: Current date for timestamping
        """
        FileManager.ensure_directory_exists("prompts")

        # Save timestamped version
        timestamped_path = os.path.join(FileManager.get_project_root(), "prompts", f"prompt_{current_date}.txt")
        with open(timestamped_path, "w") as f:
            f.write(prompt)
        print(f"Prompt '{timestamped_path}' saved successfully.\n")

        # Save current version
        current_path = os.path.join(FileManager.get_project_root(), "prompts", "prompt_current.txt")
        with open(current_path, "w") as f:
            f.write(prompt)
        print(f"Prompt '{current_path}' saved successfully.\n")

    @staticmethod
    def save_event(prompt: str) -> None:
        """
        Append the event line from the prompt to a file, all on the same line, each event in square brackets and separated by comma.

        Args:
            prompt: Prompt text to extract the event line from
        """
        FileManager.ensure_directory_exists("events")

        # Extract the first line (event line) and wrap in square brackets if not already
        event_line = prompt.strip().splitlines()[0].strip()
        if not (event_line.startswith("[") and event_line.endswith("]")):
            event_line = f"[{event_line}]"

        event_path = os.path.join(FileManager.get_project_root(), "events", "past_events.txt")
        # Read current content
        if os.path.exists(event_path):
            with open(event_path, "r+") as f:
                content = f.read().strip()
                if content:
                    # Remove trailing comma if present
                    content = content.rstrip(", ")
                    new_content = f"{content}, {event_line}"
                else:
                    new_content = event_line
                f.seek(0)
                f.write(new_content + "\n")
                f.truncate()
        else:
            with open(event_path, "w") as f:
                f.write(event_line + "\n")
        print(f"Event line '{event_line}' appended to '{event_path}' successfully.\n")

    @staticmethod
    def read_all_events() -> str:
        """
        Read all event lines from the event list file and return as a single string.

        Returns:
            All event lines joined as a single string, separated by newlines.
        """
        event_path = os.path.join(FileManager.get_project_root(), "events", "past_events.txt")
        if not os.path.exists(event_path):
            return ""
        with open(event_path, "r") as f:
            return f.read()

    @staticmethod
    def update_readme(prompt: str) -> None:
        """
        Update README file with the new prompt.

        Args:
            prompt: Prompt text to add to README
        """
        try:
            readme_path = os.path.join(FileManager.get_project_root(), "README.md")
            with open(readme_path, "r") as readme_file:
                readme_content = readme_file.readlines()

            updated_readme_content = []
            for line in readme_content:
                if line.strip() == "![screenshot](images/panda_current.png)":
                    updated_readme_content.append(line)
                    updated_readme_content.append(f"\n**Prompt:** {prompt}\n")
                    break
                else:
                    updated_readme_content.append(line)

            with open(readme_path, "w") as readme_file:
                readme_file.writelines(updated_readme_content)

            print("README updated successfully.\n")

        except FileNotFoundError:
            print("Warning: README.md not found, skipping README update.")

