Setup instructions :
          • Create and activate a virtual environment
              python -m venv venv
              venv\Scripts\activate     
          •  Install dependencies
                pip install:
                  Django==4.2.23
                  django-bootstrap-v5==1.0.11
                  mysqlclient==2.2.7
          •  Configure database
                •	Update settings.py with your database credentials (MySQL).
                •	Run migrations:
                •	python manage.py migrate
          •  Create a admin account
                python manage.py createsuperuser
         
          •  Start the server
                python manage.py runserver
                •  Access the application
                •	Open http://127.0.0.1:8000/ in your browser.
                •	Login using the teacher credentials.


List of Features:

             • Authentication:
          
                • Teacher login with custom password hashing (manual SHA-256 with salt).
                  Manual session handling using tokens and cookies.
          
           • Teacher Home / Dashboard:
              • View list of students with:
                  Name
                  Subject
                  Marks
              • Inline editing of student marks.
              • Inline deletion of student records.
          
           • Student Management:
                • Add new student via modal form.
                • If a student with the same name & subject exists
                • Update marks using calculate_new_marks(old, new)
                • Prevent insertion if marks exceed 100
                • Reject invalid inputs (negative marks, >100).
          
           • Validation & Audit Logging:
                • Server-side validation for all updates.
                 •Automatic logging of updates with:
                    Timestamp
                    Teacher info(id)
                    New_mark
                    student info(id)
          
           • Security:
          
                • Input validation on both client and server.
                • Passwords stored in salted, hashed format.
                • CSRF & XSS protection.
          

Security considerations :
          •  Custom Session Handling:
                 Session tokens generated using (hex encoded).Tokens stored in memory with expiry timestamps.
                 Tokens sent to client via secure HttpOnly cookies.
           • Authentication:
                 Login with username & password (hashed using SHA-256 with salt).
                 Logout clears session both in memory and cookie.Protected views validate session token before granting access.
           • Form Validation & Error Messages:
                Django forms for safe input validation.Error messages displayed dynamically and auto-hidden using JavaScript.
           • Security Enhancements:
                 Passwords stored as salted hashes.Cookies set with HttpOnly and SameSite flags.Session expiry (30 minutes idle timeout).

Challenges Faced:

        •  Manual Session Management:
            Implementing token generation, expiry checks, and cleanup.
            Ensuring secure handling of cookies without Django’s built-in session middleware.

Approximate Time Taken:
           • 2 days  taken to completete the talk.
