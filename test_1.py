from requests import get

print(get('http://127.0.0.1:8080/api/jobs').json())  # get all jobs
print(get('http://127.0.0.1:8080/api/jobs/1').json())  # get single job (valid)
print(get('http://127.0.0.1:8080/api/jobs/999').json())  # get single job (invalid - not found id)
print(get('http://127.0.0.1:8080/api/jobs/q'))  # get single job (invalid - string instead of int)
