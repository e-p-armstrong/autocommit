import subprocess
import time
import yaml
from openai import OpenAI

# Helper function stub
def process_diff_output(diff_output,client):
    # Process the diff output here and return a commit message
    example_messages = [
        {
            "role": "system",
            "content": """You are an expert Git commit message writer and programmer who always follows best practices when it comes to git commit names. You write descriptive and minimal git commit names based on provided git diffs that fully encapsulate the changes made to the code.""",
        },
        {
            "role": "user",
            "content": """diff --git a/serialization.py b/serialization.py
index 29348ab..4f21cde 100644
--- a/serialization.py
+++ b/serialization.py
@@ -45,7 +45,10 @@ def serialize_user_data(user_data):
         return json.dumps(user_data)
     except TypeError as e:
-        logger.error(f"Failed to serialize user data: {e}")
+        # Attempt to handle serialization of custom objects
+        if hasattr(user_data, '__dict__'):
+            return json.dumps(user_data.__dict__)
+        else:
+            logger.error(f"Failed to serialize user data: {e}")
         raise SerializationError("User data serialization failed")

diff --git a/utils.py b/utils.py
index cde45ab..34f2abc 100644
--- a/utils.py
+++ b/utils.py
@@ -101,3 +101,4 @@ def helper_function(args):
     pass

+# Minor typo fix
+def another_util_function():
-    print("Helo World")
+    print("Hello World")
\ No newline at end of file
""",
        },
        {
            "role": "assistant",
            "content": """Partial fix for user data serialization bug (WIP), plus typo in utils""",
        },
        {
            "role": "user",
            "content": """diff --git a/auth.js b/auth.js
new file mode 100644
index 0000000..e4f2b3c
--- /dev/null
+++ b/auth.js
@@ -0,0 +1,35 @@
+// Authentication module
+export class Auth {
+    constructor() {
+        this.users = []; // Placeholder for user storage
+    }
+
+    login(username, password) {
+        const user = this.users.find(u => u.username === username && u.password === password);
+        if (user) {
+            console.log("Login successful");
+            return true;
+        } else {
+            console.log("Login failed");
+            return false;
+        }
+    }
+
+    logout() {
+        console.log("User logged out");
+    }
+
+    resetPassword(username, oldPassword, newPassword) {
+        const userIndex = this.users.findIndex(u => u.username === username && u.password === oldPassword);
+        if (userIndex !== -1) {
+            this.users[userIndex].password = newPassword;
+            console.log("Password reset successful");
+            return true;
+        } else {
+            console.log("Password reset failed");
+            return false;
+        }
+    }
+}

diff --git a/logger.js b/logger.js
index 4f21cde..29348ab 100644
--- a/logger.js
+++ b/logger.js
@@ -28,5 +28,6 @@ export function info(message) {
     console.log(`INFO: ${message}`);
 }

+// Added debug logging functionality
 export function debug(message) {
     console.log(`DEBUG: ${message}`);
 }
""",
        },
        {
            "role": "assistant",
            "content": """Add new authentication module with login, logout, and password reset functions; add debug log function""",
        },{
            "role": "user",
            "content": """diff --git a/async_processor.py b/async_processor.py
new file mode 100644
index 0000000..e4f2c3b
--- /dev/null
+++ b/async_processor.py
@@ -0,0 +1,23 @@
+# Asynchronous Data Processor
+import asyncio
+
+# TODO: Implement the main processing function
+async def process_data(data):
+    print("Starting data processing...")
+    # Debugging line
+    print(f"Processing {data}")
+    # Placeholder for actual processing logic
+    await asyncio.sleep(1)  # Simulate async operation
+    print("Data processed")
+
+# Alternative approach (commented out for now)
+# def process_data_sync(data):
+#     print("Synchronous processing not implemented")
+
+if __name__ == "__main__":
+    data = "sample data"
+    # Debugging line below
+    print(f"Debug: Initial data {data}")
+    asyncio.run(process_data(data))
+
diff --git a/utils.py b/utils.py
index 34f2abc..cde45ab 100644
--- a/utils.py
+++ b/utils.py
@@ -104,3 +104,4 @@ def another_util_function():
     print("Hello World")
 
+# Added a placeholder for future utility function
+def future_util():
+    pass  # TODO: Implement this function
\ No newline at end of file

diff --git a/config/settings.py b/config/settings.py
index 1f34bac..4b21fa3 100644
--- a/config/settings.py
+++ b/config/settings.py
@@ -15,6 +15,7 @@
 DATABASE_URI = "database-uri-placeholder"
 
+# Temporary debug mode flag
+DEBUG_MODE = True
 
diff --git a/templates/base.html b/templates/base.html
index 2a4b6c8..3d5f4e7 100644
--- a/templates/base.html
+++ b/templates/base.html
@@ -14,6 +14,7 @@
         <title>Sample App</title>
     </head>
     <body>
+        <!-- Temporary message for development -->
+        <p>Under construction</p>
         {% block content %}
         {% endblock %}
     </body>

diff --git a/.DS_Store b/.DS_Store
new file mode 100644
index 0000000..d41d8cd
Binary files /dev/null and b/.DS_Store differ
""",
        },
        {
            "role": "assistant",
            "content": """Start async data processing feature; misc updates in utils, settings, and base template""",
        },{
            "role": "user",
            "content": f"""{diff_output}""",
        }
    ]

    completion = client.chat.completions.create(
        messages=example_messages,
        model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
    ).choices[0].message.content
    return completion

# Function to execute shell commands in a specified directory
def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, text=True, capture_output=True, cwd=cwd)
    return result.stdout.strip()

# Main function to periodically diff and commit
def main(config_path):
    # Load configuration
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    client = OpenAI(
        api_key=config["api_key"], base_url=config["base_url"]
    )
    
    repo_path = config['repo_path']
    interval_seconds = config['interval_seconds']
    
    while True:
        print(f"Committing in {repo_path}...")

        add_output = run_command('git add .', cwd=repo_path)
        # Add all changes
        # print(add_output)
        
        # Perform git diff
        diff_output = run_command('git diff HEAD', cwd=repo_path)
        # print(diff_output)
        
        if not diff_output:
            print("No changes, sleeping")
            time.sleep(interval_seconds)
            continue
        
        # Process the diff output through the helper function
        commit_message = process_diff_output(diff_output,client)
        
        # Commit changes
        commit_output = run_command(f'git commit -m "{commit_message}"', cwd=repo_path)
        print(commit_output)
        print(f"Committed with message: '{commit_message}'")
        
        if config["push"]:
            push_output = run_command(f'git push',cwd=repo_path)
            print(push_output)
            print("Pushed!")

        # Wait for the specified interval
        time.sleep(interval_seconds)

if __name__ == "__main__":
    config_file_path = "config.yaml"  # Specify the path to your YAML config file
    main(config_file_path)
