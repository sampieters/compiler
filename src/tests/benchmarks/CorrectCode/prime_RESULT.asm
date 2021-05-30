.data
string1_1: .asciiz "Enter the number of prime numbers required\n\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "First "
string3_2: .asciiz " prime numbers are :\n\00"
string4_1: .asciiz "2\n\00"
string5_1: .asciiz ""
string5_2: .asciiz "\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -56
        sw      $fp, 52($sp)
        sw      $ra, 48($sp)
        sw      $4, 44($sp)
        move    $fp, $sp
        li      $8, 3
        sw      $8, 4($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        la      $4, string2_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 0($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        # BEGIN IF CONDITION
        lw      $9, 0($fp)
        sge     $9, $9, 1
        sw      $9, 16($fp)
        lw      $9, 16($fp)
        beq     $9,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        la      $4, string4_1
        li      $v0, 4
        syscall 
        # END IF BODY
$L0:    
        li      $9, 2
        li      $10, 2
        sw      $10, 20($fp)
                
$L1:    
        # BEGIN WHILE CONDITION
        lw      $10, 20($fp)
        lw      $11, 0($fp)
        sle     $10, $10, $11
        sw      $10, 24($fp)
        lw      $10, 24($fp)
        beq     $10, $0, $L6
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        li      $10, 2
        li      $11, 2
        sw      $11, 28($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $11, 4($fp)
        subi    $11, $11, 1
        lw      $11, 28($fp)
        sle     $11, $11, $11
        sw      $11, 32($fp)
        lw      $11, 32($fp)
        beq     $11, $0, $L4
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        # BEGIN IF CONDITION
        lw      $11, 4($fp)
        lw      $12, 28($fp)
        NIET ZOMAAR$11, $11, $12
        seq     $11, $11, 0
        sw      $11, 36($fp)
        lw      $11, 36($fp)
        beq     $11,$0, $L3
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        j       $L4
        # END IF BODY
$L3:    
        lw      $11, 28($fp)
        addiu   $11, $11, 1
        sw      $11, 28($fp)
        j       $L2
        # END WHILE BODY
                
$L4:    
        # BEGIN IF CONDITION
        lw      $11, 28($fp)
        lw      $12, 4($fp)
        seq     $11, $11, $12
        sw      $11, 40($fp)
        lw      $11, 40($fp)
        beq     $11,$0, $L5
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $11, 20($fp)
        addiu   $11, $11, 1
        sw      $11, 20($fp)
        # END IF BODY
$L5:    
        lw      $11, 4($fp)
        addiu   $11, $11, 1
        sw      $11, 4($fp)
        j       $L1
        # END WHILE BODY
                
$L6:    
        move    $sp, $fp
        lw      $4, 44($sp)
        lw      $ra, 48($sp)
        lw      $fp, 52($sp)
        addiu   $sp, $sp, 56
        li      $v0, 10
        syscall 