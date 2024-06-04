-- 코드를 입력하세요
# SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE "%Neutered%" OR "%Spayed%", "O", "X") AS 중성화
# FROM ANIMAL_INS
# ORDER BY ANIMAL_ID;    

SELECT ANIMAL_ID,NAME,
    case when SEX_UPON_INTAKE like "%Neutered%" then "O"
    when SEX_UPON_INTAKE like "%Spayed%" then "O"
    else "X" end as "중성화"
from ANIMAL_INS