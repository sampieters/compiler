.data
string1_1: .asciiz "Enter a 5-character string:\00"
string2_1: .asciiz "%5s\00"
string3_1: .asciiz ""
string3_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 4($fp)
        addiu   $8, $fp, 4
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $8, 12($fp)
        lw      $4, 12($fp)
        li      $v0, None
        syscall 
        sw      $None, 4($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, None
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 