# Start to learn Authentication on Flask

1. Cookies (cookie save on client browser) =>authlesson1.py

    In Flask, cookies are set on response object. Use make_response() function to get response object from return value of a view function. After that, use the set_cookie() function of response object to store a cookie.
    Reading back a cookie is easy. The get() method of request.cookies attribute is used to read a cookie.

2. Session (Session save on server) => authlesson2.py
    Similar with Cookie, but the data save on browser
    