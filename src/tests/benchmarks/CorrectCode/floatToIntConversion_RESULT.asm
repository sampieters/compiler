.data
float1: .float 5.000000e-01
string1_1: .asciiz ""
string1_2: .asciiz " "
string1_3: .asciiz " "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        l.s     $f4, float1
        s.s     $f4, 4($fp)
        lw      $f5, 4($fp)
        sw      $f5, 8($fp)
        li      $8, 0
        sw      $8, 12($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 2
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_3
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_4
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 