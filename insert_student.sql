SELECT * FROM student_list;

INSERT INTO student_list(id, name, email, phone)
VALUES (1, "Riley", "serialraider117@gmail.ed", "+1 6832 1292")

INSERT INTO student_list(id, name, email, phone)
VALUES (2, "Ray", "DATA LOST", "DATA LOST")

DELETE FROM student_list WHERE id=2;

UPDATE student_list SET name="Riley Henderson", email="serialraider117@thenightraider.com", phone="DATA LOST" WHERE id=1

