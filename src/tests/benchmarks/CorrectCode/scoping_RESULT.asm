.data
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
        x       .TYPE VALUE
        x       .TYPE VALUE
        li      $8, 10
        sw      $8, 4($fp)
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 20($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        li      $9, 20
        sw      $9, 8($fp)
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 4
        syscall 
        li      $10, 30
        sw      $10, 12($fp)
        # BEGIN IF CONDITION
        beq     REGISTER, $0, $L0
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
        li      $11, 40
        sw      $11, 16($fp)
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
        nop     
        move    $sp, $fp
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 