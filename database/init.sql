create table users
(
    row_id  integer generated always as identity primary key,
    user_id integer    not null unique,
    name    varchar not null,
    company varchar not null,
    address varchar not null,
    city    varchar not null
);

insert into users (user_id, name, company, address, city)
VALUES (123, 'Chancellor Watkins', 'Tellus Justo PC', '461-7086 Amet, Rd.', 'Tobermory'),
       (456, 'Tamekah Moon', 'Penatibus Et Industries', 'P.O. Box 798, 950 Sit Road', 'Muong Lay'),
       (234, 'Talon Harrell', 'Sed Eu Institute', 'Ap #666-276 Aliquam Ave', 'Stratford-upon-Avon'),
       (4563, 'Emmanuel Giles', 'A Odio Corporation', '150-5440 Fringilla Ave', 'Naperville'),
       (523, 'Kermit Potter', 'Nullam Enim PC', '719-3428 Phasellus St.', 'Diadema');
