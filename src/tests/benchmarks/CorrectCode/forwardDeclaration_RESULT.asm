.data
string1_1: .asciiz "Hello \00"
string2_1: .asciiz "World\n\00"
string3_1: .asciiz "World\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        jr      $ra
                
g:      
        addiu   $sp, $sp, -16
        sw      $fp, 12($sp)
        sw      $ra, 8($sp)
        sw      $4, 4($sp)
        move    $fp, $sp
        la      $4, string2_1
        li      $v0, 4
        syscall 
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        move    $sp, $fp
        lw      $4, 4($sp)
        lw      $ra, 8($sp)
        lw      $fp, 12($sp)
        addiu   $sp, $sp, 16
        jr      $ra
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        sw      $ra, 12($sp)
        sw      $4, 8($sp)
        move    $fp, $sp
        jal     f
        jal     g
        move    $sp, $fp
        lw      $4, 8($sp)
        lw      $ra, 12($sp)
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 