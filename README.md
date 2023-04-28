
## Send Email with Attachment in Outlook using Python

This Python code demonstrates how to send an email with an attachment in Outlook using Python's built-in `smtplib` and `email` libraries.

### Prerequisites

-   Python 3.x installed on your machine.
-   An email account with Outlook that allows programmatic access.

### Getting Started

1.  Clone or download the repository to your local machine.
2.  Open the `singleFile.py` file in your preferred code editor.
3.  Replace the following placeholders with your own values:
    -   `smtp_server`: the SMTP server for your email provider.
    -   `smtp_username`: the email address you want to use to send the email.
    -   `smtp_password`: the password for the email address you want to use to send the email.
    -   `sender_email`: the email address you want to use to send the email.
    -   `recipient_email`: the email address you want to send the email to.
    -   `email_subject`: the subject line of the email.
    -   `email_body`: the body text of the email.
    -   `attachment_path`: the file path of the attachment you want to include in the email.
4.  Save the changes to the `singleFile.py` file.
5.  Open a terminal or command prompt and navigate to the directory where the `singleFile.py` file is located.
6.  Run the following command to execute the script: `python singleFile.py`.

### Sending Email with Attachment for Multiple Files

If you want to send an email with an attachment for multiple files in a folder, you can use the `multipleFiles.py` script instead. This script uses the same `smtplib` and `email` libraries as the previous script, but it also uses the `os` and `glob` libraries to iterate over the files in a folder and send an email with an attachment for each file.

To use the `multipleFiles.py` script, follow the same steps as before, but replace the `singleFile.py` file with the `multipleFiles.py` file and replace the `folder_path` variable with the path to the folder containing the files you want to send as attachments.
