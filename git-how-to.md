#Как создать ssh ключ?
Вызвать команду: ssh-getkey -t ed25519 -C "тут должна быть твоя почта"
Что такое ed25519? А черт его знает
#Как добавить ключ ключ в аккаунт на github?
Потыкаться в интерфейсе github и найти что то про ключи ssh и GPG -> туда сунуть тектс из файла, созданного прежде с расширением .pub
#Как скопировать репозиторий?
git clone git@github.com:имя_юзера_на_github/название_репозитория.git
