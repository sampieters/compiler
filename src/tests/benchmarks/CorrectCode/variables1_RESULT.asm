.data
double1: .double 5.000000e-01
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        l.d     $f4, double1
        s.d     $f4, 4($fp)
        li      $8, 99
        sb      $8, 12($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        l.d     $f12, 4($fp)
        li      $v0, 3
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        lb      $4, 12($fp)
        li      $v0, 11
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 