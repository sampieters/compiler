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
        addiu   $sp, $sp, -20
        sw      $fp, 16($sp)
        sw      $ra, 12($sp)
        sw      $4, 8($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, x
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        li      $8, 20
        sw      $8, 0($fp)
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        li      $8, 30
        sw      $8, 0($fp)
        # BEGIN IF CONDITION
        li      $8, 1
        beq     $8, $0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        li      $9, 40
        sw      $9, 4($fp)
        la      $4, string4_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        li      $2, 1
        syscall 
        la      $4, string4_2
        li      $2, 4
        syscall 
        # END IF BODY
$L0:    
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 8($sp)
        lw      $ra, 12($sp)
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $2, 10
        syscall 