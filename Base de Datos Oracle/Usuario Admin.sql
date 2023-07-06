alter session set "_ORACLE_SCRIPT"=true;
create user django identified by "123456";
grant connect, resource to django;
alter user django default tablespace users quota unlimited on users;