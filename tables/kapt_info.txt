drop table if exists kapt_list;
create table if not exists kapt_list
(
lawd_cd varchar(10) not null comment '법정동 코드',
kapt_cd varchar(10) not null comment '아파트코드',
kapt_nm varchar(30) not null comment '아파트이름',
primary key (lawd_cd, kapt_cd)
) comment '국토교통부-공동주택단지목록';

drop table if exists kapt_info;
create table if not exists kapt_info
(
lawd_cd        varchar(10)  not null comment '법정동 코드',
kapt_cd        varchar(10)  not null comment '아파트코드',
kapt_nm        varchar(30)  not null comment '아파트이름',
kapt_da_cnt    int                   comment '세대수',
kapt_dong_cnt  int                   comment '동수',
code_apt_nm    varchar(10)           comment '단지분류',
code_hall_nm   varchar(3)            comment '복도유형',
code_heat_nm   varchar(10)           comment '난방방식',
code_sale_nm   varchar(5)            comment '분양형태',
kapt_use_date  varchar(8)            comment '사용승인일',
kapt_marea_60  int                   comment '전용 60m2 이하 세대수',
kapt_marea_85  int                   comment '전용 60~85m2 이하 세대수',
kapt_marea_135 int                   comment '전용 85~135m2 이하 세대수',
kapt_marea_136 int                   comment '전용 136m2 초과 세대수',
kapt_marea     decimal(15,4)         comment '관리비부과면적(m2)',
kapt_tarea     decimal(15,4)         comment '건축물관리대장상 연면적(m2)',
priv_area      decimal(15,4)         comment '단지전용면적합',
kapt_addr      varchar(50)           comment '법정동주소',
doro_juso      varchar(30)           comment '도로명주소',
kapt_acompany  varchar(40)           comment '시행사',
kapt_bcompany  varchar(50)           comment '시공사',
code_mgr_nm    varchar(5)            comment '관리방식',
primary key (kapt_cd)
) comment '국토교통부-공동주택단지정보';

