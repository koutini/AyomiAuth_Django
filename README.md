# AyomiAuth_Django
### Installation

Uses the default Django development server.

1. clone project:
    ```sh
    git clone https://github.com/koutini/AyomiAuth_Django.git
    cd AyomiAuth_Django
    ```
2. build images 
    ```sh
    1/docker-compose up -d --build postgres_db
    2/docker-compose up  --build app
    ```
Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

That's it!, you can register to create new user or create superuser to login: 
  ```sh
  ./ manage.py createsuperuser 
  ```
