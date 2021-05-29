.data
string1_1: .asciiz "Enter the number of prime numbers required\0A\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "First "
string3_2: .asciiz " prime numbers are :\0A\00"
string4_1: .asciiz "2\0A\00"
string5_1: .asciiz ""
string5_2: .asciiz "\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        li      $8, 3
        sw      $8, 4($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $9, 2($fp)
        addiu   $10, $fp, 2
        la      $4, string2_1
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
        # BEGIN IF CONDITION
        lw      $11, 2($fp)
        sgei    $12, $11, 1
        beq     REGISTER, $0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 2($fp)
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
        li      $13, 2
        sw      $13, 8($fp)
                
$L1:    
        # BEGIN WHILE CONDITION
        lw      $14, 4($fp)
        lw      $24, 2($fp)
        sle     $Error, $14, $24
        beq     $Error, $0, {LABEL}
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        li      $Error, 2
        sw      $Error, 12($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $Error, 0($fp)
        subi    $Error, $Error, 1
        lw      $Error, 5($fp)
        sle     $Error, $Error, $Error
        beq     $Error, $0, $L6
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        # BEGIN IF CONDITION
        lw      $Error, 0($fp)
        lw      $Error, 5($fp)
        NIET ZOMAAR$Error, $Error, $Error
        seqi    $Error, $Error, 0
        beq     REGISTER, $0, $L4
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        j       ${BREAK}
        # END IF BODY
$L3:    
        lw      $Error, 5($fp)
        addiu   $Error, $Error, 1
        j       $L2
        # END WHILE BODY
                
$L4:    
        # BEGIN IF CONDITION
        lw      $Error, 5($fp)
        lw      $Error, 0($fp)
        seq     $Error, $Error, $Error
        beq     REGISTER, $0, $L5
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $Error, 4($fp)
        addiu   $Error, $Error, 1
        # END IF BODY
$L5:    
        lw      $Error, 0($fp)
        addiu   $Error, $Error, 1
        j       $L1
        # END WHILE BODY
                
$L6:    
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 