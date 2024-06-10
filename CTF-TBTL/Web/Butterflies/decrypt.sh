# Após encontrar local Storage -> pass secret key is very secure
# Encontrar IndexedDB do site a cifra codificada

echo 'U2FsdGVkX19wWL7itIL7TZcLTP/e1ulrZolI9AHTA8OBGOCodbZKdOxPF41rGV9C+X7PZPt9ISJKQMpTl+Fwew==' | openssl enc -aes-256-cbc -d -a -md md5 -pass pass:"secret key is very secure"