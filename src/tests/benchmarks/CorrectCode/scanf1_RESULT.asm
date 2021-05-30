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
        addiu   $sp, $sp, -28
        sw      $fp, 28($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 4($fp)
        addiu   $8, $fp, 4
        lw      $8, 8($fp)
        addiu   $8, $fp, 8
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $8, 16($fp)
        lw      $4, 16($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 4($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        sw      $8, 24($fp)
        lw      $4, 24($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 8($fp)
        la      $4, string2_3
        li      $v0, 4
        syscall 
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_3
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $v0, 10
        syscall 