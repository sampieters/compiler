.data
string1_1: .asciiz ""
string1_2: .asciiz " "
string1_3: .asciiz "!\n\00"
string2_1: .asciiz "Hello\00"
string3_1: .asciiz "World\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        la      $4, string2_1
        li      $2, 4
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        la      $4, string3_1
        li      $2, 4
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $2, 10
        syscall 