.data
string1_1: .asciiz "Enter two numbers:\00"
string2_1: .asciiz ""
string2_2: .asciiz ""
string2_3: .asciiz "\00"
string3_1: .asciiz ""
string3_2: .asciiz "; "
string3_3: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        sw      $ra, 12($sp)
        sw      $4, 8($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 5
        syscall 
        sw      $v0, 0($fp)
        la      $4, string2_2
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        li      $2, 5
        syscall 
        sw      $v0, 4($fp)
        la      $4, string2_3
        li      $2, 4
        syscall 
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        li      $2, 1
        syscall 
        la      $4, string3_3
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 8($sp)
        lw      $ra, 12($sp)
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $2, 10
        syscall 