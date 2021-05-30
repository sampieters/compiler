.data
string1_1: .asciiz "Hello \00"
string2_1: .asciiz "World\n\00"
string3_1: .asciiz "World\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -4
        sw      $fp, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 0($sp)
        addiu   $sp, $sp, 4
        jr      $ra
                
g:      
        addiu   $sp, $sp, -8
        sw      $fp, 4($sp)
        move    $fp, $sp
        la      $4, string2_1
        li      $v0, 4
        syscall 
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        jr      $ra
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        move    $fp, $sp
        jal     f
        jal     g
        move    $sp, $fp
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $v0, 10
        syscall 