.data
string1_1: .asciiz ""
string1_2: .asciiz ""
string1_3: .asciiz ""
string1_4: .asciiz "\00"
double1: .double 5.000000e-01
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        li      $4, 10
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        l.d     $f12, double1
        li      $2, 3
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        li      $4, 37
        li      $2, 11
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 16
        li      $2, 10
        syscall 