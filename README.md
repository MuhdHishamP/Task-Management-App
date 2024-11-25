# Task Management App with Google Login

This is a web application built using Django that enables users to manage personal tasks after logging in with their Google account. The app provides features for task management, admin configuration, and user invitation via email.

You can access the live version of the app here: <a href="https://task-management-app-kappa-bay.vercel.app/" target="_blank">Task Management App</a>


## Features

### 1. Google Authentication
- Users can securely log in using their Google accounts.

### 2. Task Management
- Create, view, edit, and delete tasks.
- Each task includes a title and description.

### 3. Admin Panel
- Admins can manage Google OAuth keys directly in the admin interface.
- Admins can invite new users by sending an email with a registration link.

## Demo Videos


https://github.com/user-attachments/assets/932ec83c-c761-434c-b1b8-53a5009ab1e7

https://github.com/user-attachments/assets/16e69b9f-a5dd-4e2e-a0a0-b13b349fa2e9

## Setup Instructions

Follow these steps to set up the Task Management App:

1. Clone the repository:
   ```bash
   git clone https://github.com/MuhdHishamP/Task-Management-App.git
   cd Task-Management-App
   ```

2. Configure email settings in `settings.py`:
   - `EMAIL_HOST_USER`
   - `DEFAULT_FROM_EMAIL`

3. Set up environment variables in `settings.py`:
   - `DATABASE_URL`
   - `EMAIL_HOST_PASSWORD`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```


## Notes
- The app requires a properly configured Google Cloud project for OAuth credentials.
- Email functionality depends on correct configuration of related settings.
- Ensure the .env file is not exposed in your repository for security.
