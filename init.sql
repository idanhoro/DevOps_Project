
create table if not exists randoms(
    entry_id int auto_increment, 
    random_num int not null,
    created_at timestamp default current_timestamp,
    primary key(entry_id)
);

GRANT ALL PRIVILEGES ON 'randoms.app' TO 'app'@'%';
