.data
string1: .asciiz "%d%f%c\00"
double1: .double 5.000000e-01
.globl main
.text
                
main:   
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $6,string1
        li      $6,10
        l.d     $None,double1
        li      $6,37
        li      $6,10
        li      $v0,1
        syscall 
        l.d     $None,double1
        li      $v0,3
        syscall 
        li      $6,37
        li      $v0,11
        syscall 
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        li      $v0,10
        syscall 