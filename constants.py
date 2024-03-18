COLUMNS_USERNAME_SIZE = 32
COLUMN_EMAIL_SIZE = 255

# 4kb since 1 kb is equal to 1024 bytes so 4*1024 = 4096
# each byte represents 8 bits so 1024 * 8 = 8192 bits * 4 = 32768 bits. 
PAGE_SIZE = 4096 
TABLE_MAX_PAGES = 100