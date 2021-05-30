.data
string1_1: .asciiz "Enter a 5-character string:\00"
string2_1: .asciiz "%5s\00"
string3_1: .asciiz ""
string3_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -13
        sw      $fp, 13($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 1($fp)
        addiu   $8, $fp, 1
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $8, 9($fp)
        lw      $4, 9($fp)
        li      $v0, None
        syscall 
        sw      $None, 1($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 1($fp)
        li      $v0, None
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        nop     
        move    $sp, $fp
        lw      $fp, 13($sp)
        addiu   $sp, $sp, 17
        li      $v0, 10
        syscall 