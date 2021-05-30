.data
x: .word  10
string1_1: .asciiz ""
string1_2: .asciiz ";\00"
string2_1: .asciiz ""
string2_2: .asciiz ";\00"
string3_1: .asciiz ""
string3_2: .asciiz ";\00"
string4_1: .asciiz ""
string4_2: .asciiz ";\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 20($sp)
        sw      $ra, 16($sp)
        sw      $4, 12($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, x
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        li      $8, 20
        sw      $8, 0($fp)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        li      $8, 30
        li      $9, 30
        sw      $9, 4($fp)
        # BEGIN IF CONDITION
        li      $9, 1
        beq     $9,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        li      $10, 40
        sw      $10, 8($fp)
        la      $4, string4_1
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string4_2
        li      $v0, 4
        syscall 
        # END IF BODY
$L0:    
        li      $v0, 1
        move    $sp, $fp
        lw      $4, 12($sp)
        lw      $ra, 16($sp)
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 