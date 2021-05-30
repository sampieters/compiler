.data
string1_1: .asciiz ""
string1_2: .asciiz ""
string1_3: .asciiz ""
string1_4: .asciiz "\00"
double1: .double 5.000000e-01
.globl main
.text
                
main:   
        addiu   $sp, $sp, -4
        sw      $fp, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        li      $4, 10
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        l.d     $f12, double1
        li      $v0, 3
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        li      $4, 37
        li      $v0, 11
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 0($sp)
        addiu   $sp, $sp, 4
        li      $v0, 10
        syscall 