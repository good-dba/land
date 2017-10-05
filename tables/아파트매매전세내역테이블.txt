drop table if exists deal_history;
create table if not exists deal_history
(
no          int          not null auto_increment,
sgg_cd      varchar(5)   not null comment '지역코드(법정동코드=lawd_cd 앞5글자)',
law_dong_nm varchar(10)  not null comment '법정동명',
lawd_cd     varchar(10)           comment '법정동 코드',
apt_nm      varchar(50)  not null comment '아파트이름',
deal_ym     varchar(6)   not null comment '거래년월',
deal_dd     varchar(5)   not null comment '거래일(10일단위 구간)',
priv_area   varchar(30)  not null comment '전용면적',
deal_amount int not null comment '거래금액',
built_yyyy  varchar(4)   not null comment '건축년도',
post_no     varchar(10)   not null comment '지번',
floor       int not null comment '층',
primary key (no),
index idx_lawd (sgg_cd, law_dong_nm),
index idx_apt_nm (apt_nm),
index idx_deal_ym (deal_ym),
index idx_lawd_cd (lawd_cd)
) comment '국토교통부-아파트매매이력';

drop table if exists rent_history;
create table if not exists rent_history
(
no             int          not null auto_increment,
sgg_cd         varchar(5)   not null comment '지역코드(법정동코드=lawd_cd 앞5글자)',
law_dong_nm    varchar(10)  not null comment '법정동명',
lawd_cd        varchar(10)           comment '법정동 코드',
apt_nm         varchar(50)  not null comment '아파트이름',
deal_ym        varchar(6)   not null comment '거래년월',
deal_dd        varchar(5)   not null comment '거래일(10일단위 구간)',
priv_area      varchar(30)  not null comment '전용면적',
deposit_amount int          not null comment '보증금액',
m_rent_amount  int          not null comment '월세금액',
built_yyyy     varchar(4)   not null comment '건축년도',
post_no        varchar(10)   not null comment '지번',
floor          int not null comment '층',
primary key (no),
index idx_lawd (sgg_cd, law_dong_nm),
index idx_apt_nm (apt_nm),
index idx_deal_ym (deal_ym),
index idx_lawd_cd (lawd_cd)
) comment '국토교통부-아파트전월세이력';

