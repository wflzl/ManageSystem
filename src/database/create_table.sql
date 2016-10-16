CREATE TABLE T_GOODS(
    GOOD_ID integer PRIMARY KEY NOT NULL, /*货物id标识*/
    GOOD_NAM TEXT , /*货物名称*/
    GOOD_DESC TEXT,  /*货物描述*/
    GOOD_PRICE REAL, /*货物进价*/
    SUPPLIER TEXT, /*厂商*/
    SUP_TEL TEXT, /*厂商联系方式*/
    BUY_TM TEXT /*进货时间*/
)
