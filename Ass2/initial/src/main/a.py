DELIMITER $$
DROP PROCEDURE IF EXISTS get_test_of_subject $$
CREATE PROCEDURE get_test_of_subject(IN semesterID int(11))
BEGIN
SELECT * FROM main_multiple_choice_test
WHERE TestID = (SELECT TestID )
WHERE StudentID = studentID AND TestID = testID
END
$$

DELIMITER $$
DROP PROCEDURE IF EXISTS get_student_in_semester $$
CREATE PROCEDURE get_student_in_semester(IN years year(4), IN sem_name varchar(50), IN name_sub varchar(255))
BEGIN
SELECT * FROM student
WHERE StudentID =
(SELECT STUDENTID FROM learn
 WHERE SubjectID=(SELECT SubjectID FROM subject
                  WHERE SemesterID=(SELECT SemesterID FROM semester WHERE SemesterYear=years AND SemesterName=sem_name) AND SubjectName=name_sub))
END
$$
CALL get_student_in_semester(2020, 'HK192', 'DSA')
