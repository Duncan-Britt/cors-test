The purpose of this repository is to reproduce a bug that seems to exist on M series macs.

## Reproduceability
The repo consists of a python flask api and a simple front end for testing. 

Clone the repository and start the backend with python3.

``` shell
~ $ git clone https://github.com/Duncan-Britt/cors-test.git
Cloning into 'cors-test'...
remote: Enumerating objects: 5, done.        
remote: Counting objects: 100% (5/5), done.        
remote: Compressing objects: 100% (4/4), done.        
remote: Total 5 (delta 0), reused 5 (delta 0), pack-reused 0        
Receiving objects: 100% (5/5), done.
~ $ cd cors-test/
~/cors-test $ python3 app.py 
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

```

Then serve the frontend directory at port 8080 number (or other) with your desired method and visit http://localhost:8080 . Open the developer tools and observe the error message upon attempting to make a request.
