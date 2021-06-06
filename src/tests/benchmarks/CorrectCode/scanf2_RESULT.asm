.data
string1_1: .asciiz "Enter a 5-character string:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz ""
string3_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        addiu   $8, $fp, 0
        la      $4, string2_1
        li      $2, 4
        syscall 
        move    $4, $8
        li      $5, 6
        li      $2, 8
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        la      $4, string3_1
        li      $2, 4
        syscall 
        la      $4, 0($fp)
        li      $2, 4
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 