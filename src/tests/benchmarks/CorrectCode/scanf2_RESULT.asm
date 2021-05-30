.data
string1_1: .asciiz "Enter a 5-character string:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz ""
string3_2: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -17
        sw      $fp, 13($sp)
        sw      $ra, 9($sp)
        sw      $4, 5($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, None
        syscall 
        sw      $None, 0($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, None
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $4, 5($sp)
        lw      $ra, 9($sp)
        lw      $fp, 13($sp)
        addiu   $sp, $sp, 17
        li      $v0, 10
        syscall 