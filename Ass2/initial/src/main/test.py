DELIMITER $$
DROP PROCEDURE IF EXISTS get_rate_true_false_in_question_test $$
CREATE PROCEDURE get_rate_true_false_in_question_test(IN question_id int(11), IN ver int(11), IN test_id, IN years year(4), IN sem_name varchar(50), IN name_sub varchar(255))
BEGIN
SET @ key = (SELECT GROUP_CONCAT(AnswerID) FROM answer
             WHERE Result=1 AND QuestionID=question_id AND Version=ver
             )

SET @ list = (SELECT COUNT(Answer) FROM recorded_answer
              WHERE QuestionID=question_id AND Version=ver AND Answer LIKE @ key AND TestID=test_id)
SELECT @ list as ''
END
$$

CALL get_rate_true_false_in_question_test(2, 1, 1, 2020, 'HK201', 'Kiến trúc máy tính')


DELIMITER $$
DROP PROCEDURE IF EXISTS get_rate_true_false_in_question $$
CREATE PROCEDURE get_rate_true_false_in_question(IN question_id int(11), IN ver int(11), IN years year(4), IN sem_name varchar(50), IN name_sub varchar(255))
BEGIN

	SET @ key = (SELECT GROUP_CONCAT(AnswerID) FROM answer
                WHERE Result=1 AND QuestionID=question_id AND Version=ver
    );

    SET @list = ( SELECT COUNT(Answer) FROM recorded_answer
    WHERE QuestionID = question_id AND Version = ver AND Answer LIKE @key);
    set @num_student =  get_number_student_in_semester(2020 , 'HK201' , 'Kiến trúc máy tính' );
    
	SELECT  @list *100 / @num_student as '';
    
END; $$

CALL get_rate_true_false_in_question(2 , 1 , 2020 , 'HK201' , 'Kiến trúc máy tính' )

#  Lay cac question tu mot chuan dau ra cua mot mon hoc nhat dinh
DELIMITER $$
DROP PROCEDURE IF EXISTS get_rate_true_false_in_outcome $$
CREATE PROCEDURE get_rate_true_false_in_outcome(IN )
BEGIN
	SET @key = ( SELECT GROUP_CONCAT( AnswerID) FROM answer
                WHERE Result = 1 AND QuestionID = question_id AND Version = ver
    );
	
    SET @list = ( SELECT COUNT(Answer) FROM recorded_answer
    WHERE QuestionID = question_id AND Version = ver AND Answer LIKE @key);
    set @num_student =  get_number_student_in_semester(2020 , 'HK201' , 'Kiến trúc máy tính' );
    
	SELECT  @list *100 / @num_student as '';
    
END; $$

CALL get_rate_true_false_in_question(2 , 1 , 2020 , 'HK201' , 'Kiến trúc máy tính' )


DELIMITER $$
DROP PROCEDURE IF EXISTS get_rate_of_LO $$
CREATE PROCEDURE get_rate_of_LO(IN student_id int(11), IN test_id int(11), IN outcome_id int(11))
BEGIN
       DECLARE lstQID INT(11) DEFAULT 0;
    DECLARE lstVer INT(11) DEFAULT 0;
    DECLARE lstOID INT(11) DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE numOfCorrect INT(11) DEFAULT 0;
    DECLARE numOfTotal INT(11) DEFAULT 0;
    DECLARE Momo CURSOR
     FOR
    SELECT QuestionID, Version, OutcomeID FROM Question
    WHERE (QuestionID, Version) IN (SELECT QuestionID, Version FROM attain_from
                                WHERE test_id = TestID
                                AND OutcomeID = outcome_id);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN Momo;
    get_list: LOOP
    FETCH Momo INTO lstQID, lstVer, lstOID;
    IF done THEN
        LEAVE get_list;
    END IF;
        SET @key = ( SELECT GROUP_CONCAT( AnswerID) FROM answer
                    WHERE Result = 1 AND QuestionID = lstQID AND Version = lstVer
        );
        SET @is_true = (
            SELECT COUNT(*) FROM recorded_answer
            WHERE QuestionID = lstQID 
            AND Version = lstVer 
            AND Answer LIKE @key
            AND StudentID = student_id
        );
        IF @is_true = 1 THEN
            SET numOfCorrect = numOfCorrect + 1;
        END IF;
    END LOOP get_list;
    CLOSE Momo;
    set numOfTotal = (
        SELECT COUNT(QuestionID) FROM Question
        WHERE (QuestionID, Version) IN (SELECT QuestionID, Version FROM attain_from
                                        WHERE test_id = TestID)
        AND OutcomeID = outcome_id
        GROUP BY OutcomeID
    );
    SELECT numOfCorrect/numOfTotal;
END; $$
CALL get_rate_of_LO(1811920, 1, 1)


DELIMITER $$
DROP FUNCTION IF EXISTS get_rate_of_LO_test $$
CREATE FUNCTION get_rate_of_LO_test_func( test_id int(11), outcome_id int(11))
RETURNS FLOAT
BEGIN
       DECLARE lstQID INT(11) DEFAULT 0;
    DECLARE lstVer INT(11) DEFAULT 0;
    DECLARE lstOID INT(11) DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE numOfCorrect INT(11) DEFAULT 0;
    DECLARE numOfTotal INT(11) DEFAULT 0;
    DECLARE Momo CURSOR
     FOR
    SELECT QuestionID, Version, OutcomeID FROM Question
    WHERE (QuestionID, Version) IN (SELECT QuestionID, Version FROM attain_from
                                WHERE test_id = TestID)
    AND OutcomeID = outcome_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN Momo;
    get_list: LOOP
    FETCH Momo INTO lstQID, lstVer, lstOID;
    IF done THEN
        LEAVE get_list;
    END IF;
        SET @key = ( SELECT GROUP_CONCAT( AnswerID) FROM answer
                    WHERE Result = 1 AND QuestionID = lstQID AND Version = lstVer
        );
        SET @is_true = (
            SELECT COUNT(*) FROM recorded_answer
            WHERE QuestionID = lstQID 
            AND Version = lstVer 
            AND Answer LIKE @key
        );
        SET numOfTotal = numOfTotal+1;
        IF @is_true = 1 THEN
            SET numOfCorrect = numOfCorrect + 1;
        END IF;
    END LOOP get_list;
    CLOSE Momo;
    RETURN  numOfCorrect/numOfTotal;
END; $$
SELECT get_rate_of_LO_test_func(1, 1)

DELIMITER $$
DROP PROCEDURE IF EXISTS get_rate_of_LO_test $$
CREATE PROCEDURE get_rate_of_LO_Lowest( IN test_id int(11))
BEGIN
    DECLARE lstOID INT(11) DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE numOfCorrect INT(11) DEFAULT 0;
    DECLARE numOfTotal INT(11) DEFAULT 0;
    DECLARE currents FLOAT(11) DEFAULT 0;
    DECLARE mini FLOAT(11) DEFAULT 1;
    DECLARE lowestOID INT(11) DEFAULT 0;
    DECLARE Momo CURSOR
    FOR
    SELECT DISTINCT OutcomeID FROM Question
    WHERE (QuestionID, Version) IN (SELECT QuestionID, Version FROM attain_from
                                WHERE test_id = TestID);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN Momo;
    get_list: LOOP
    FETCH Momo INTO lstOID;
    IF done THEN
        LEAVE get_list;
    END IF;
        SET currents = get_rate_of_LO_test_func(test_id,lstOID);
    IF currents <= mini THEN
        SET mini = currents;
        SET lowestOID = lstOID;
    END IF;
    END LOOP get_list;
    CLOSE Momo;
    SELECT lowestOID;
END; $$
CALL get_rate_of_LO_lowest(1)


