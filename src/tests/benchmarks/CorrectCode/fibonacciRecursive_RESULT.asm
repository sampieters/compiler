.data
string1_1: .asciiz "Enter a number:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "fib("
string3_2: .asciiz ")\09= "
string3_3: .asciiz ";\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        # BEGIN IF CONDITION
        lw      $8, 3($fp)
        slti    $8, $8, 2
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        nop     
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        lw      $8, 3($fp)
        subi    $8, $8, 1
                
        jal     f
        lw      $8, 3($fp)
        subi    $8, $8, 2
                
        jal     f
        add     $8, $11, $14
        nop     
        # END ELSE BODY
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        jr      $ra
                
main:   
        addiu   $sp, $sp, -16
        sw      $fp, 16($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 2($fp)
        addiu   $8, $fp, 2
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
        li      $8, 1
        sw      $8, 12($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $8, 12($fp)
        lw      $9, 2($fp)
        sle     $8, $8, $9
        beq     $8, $0, $L3
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $8, 12($fp)
        addi    $8, $8, 1
                
        sw      $8, 12($fp)
        lw      $4, 12($fp)
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 12($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string3_3
        li      $v0, 4
        syscall 
        j       $L2
        # END WHILE BODY
                
$L3:    
        nop     
        move    $sp, $fp
        lw      $fp, 16($sp)
        addiu   $sp, $sp, 20
        li      $v0, 10
        syscall 