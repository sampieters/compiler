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
        addiu   $sp, $sp, -40
        sw      $fp, 36($sp)
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
        sw      $9, 8($fp)
                
$L1:    
        # BEGIN WHILE CONDITION
        lw      $9, 8($fp)
        lw      $10, 0($fp)
        sle     $9, $9, $10
        sw      $9, 20($fp)
        lw      $9, 20($fp)
        beq     $9, $0, $L6
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        li      $9, 2
        sw      $9, 12($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $9, 4($fp)
        subi    $9, $9, 1
        lw      $9, 12($fp)
        sle     $9, $9, $9
        sw      $9, 24($fp)
        lw      $9, 24($fp)
        beq     $9, $0, $L4
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        # BEGIN IF CONDITION
        lw      $9, 4($fp)
        lw      $10, 12($fp)
        NIET ZOMAAR$9, $9, $10
        seq     $9, $9, 0
        sw      $9, 28($fp)
        lw      $9, 28($fp)
        beq     $9,$0, $L3
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        j       $L4
        # END IF BODY
$L3:    
        lw      $9, 12($fp)
        addiu   $9, $9, 1
        sw      $9, 12($fp)
        j       $L2
        # END WHILE BODY
                
$L4:    
        # BEGIN IF CONDITION
        lw      $9, 12($fp)
        lw      $10, 4($fp)
        seq     $9, $9, $10
        sw      $9, 32($fp)
        lw      $9, 32($fp)
        beq     $9,$0, $L5
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
        lw      $9, 8($fp)
        addiu   $9, $9, 1
        sw      $9, 8($fp)
        # END IF BODY
$L5:    
        lw      $9, 4($fp)
        addiu   $9, $9, 1
        sw      $9, 4($fp)
        j       $L1
        # END WHILE BODY
                
$L6:    
        move    $sp, $fp
        lw      $fp, 36($sp)
        addiu   $sp, $sp, 40
        li      $v0, 10
        syscall 