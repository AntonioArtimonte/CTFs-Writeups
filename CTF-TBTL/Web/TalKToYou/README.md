Basta acessar o site, notavel injeção PHP -> ?page={...}

Se colocar ?page={../../../../etc/passwd} retorna informações, mostrando que a página é sucetivel a ataques a diretórios

Colocando ?page=../../../../flag.txt, retorna em cor rgb(0,0,0,0) que a flaga está em database.sqlite

Logo basta ir em ?page=../../../../database.sqlite